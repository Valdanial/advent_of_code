def get_file_system_representation(input)
    # Returns file system as blocks, a block being a trouple: the id of file(-1 being empty), the starting address of the file, and its length
    # block[0] : File ID
    # block[1] : Block address in memory
    # block[2] : Block length
    split_line = input[0].split("") # input should be a one-liner
    blocks = []
    i = 0
    file_id_cursor = 0
    memory_cursor = 0
    for i in (0..split_line.length - 1) do
        digit = Integer(split_line[i])
        if digit > 0 then
            if i % 2 == 0 then
                # Digit defines file length
                blocks.push([file_id_cursor, memory_cursor, digit])
                file_id_cursor += 1
            else
                # Digit defines length of free space
                blocks.push([-1, memory_cursor, digit])
            end
            memory_cursor += digit
        end
    end
    return blocks
end

def get_last_block(blocks)
    last_block = nil
    for block in blocks do
        if not last_block or block[0] > last_block[0] then
            last_block = block
        end 
    end
    return last_block
end

def fuse_blocks(b1, b2)
    return [b1[0], [b1[1], b2[1]].min, b1[2] + b2[2]]
end

def fuse_adjacent_blocks(blocks, index)
    # Fuse adjacent blocks to the block at index to form a single block if file id is similar
    block = blocks[index]
    if index > 0 then
        if blocks[index][0] == blocks[index - 1][0] then
            b = fuse_blocks(blocks[index], blocks[index - 1])
            blocks[index] = b
            blocks.delete_at(index - 1)
            index -= 1
        end
    end
    if index < blocks.length - 1 then
        if blocks[index][0] == blocks[index + 1][0] then
            b = fuse_blocks(blocks[index], blocks[index + 1])
            blocks[index] = b
            blocks.delete_at(index + 1)
        end
    end
    return blocks
end

def swap_blocks_partial(blocks, i1, i2, length)
    if length == 0 then return blocks end
    [i1, i2].each {
        |i|
        if blocks[i][2] < length then
            puts "Block swap error for indexes #{i1} and #{i2} . Ignoring instruction."
            return blocks 
        end
    }
    b1 = [blocks[i1][0], blocks[i2][1] + blocks[i2][2] - length, length]
    b2 = [blocks[i2][0], blocks[i1][1], length]
    remnant_block_index = nil
    remnant_block = nil
    if blocks[i1][2] > length then
        remnant_block = [blocks[i1][0], blocks[i1][1] + length, blocks[i1][2] - length]
        remnant_block_index = i1 + 1
    elsif blocks[i2][2] > length then
        remnant_block = [blocks[i2][0], blocks[i2][1], blocks[i2][2] - length]
        remnant_block_index = i2
    end
    blocks[i1] = b2
    blocks[i2] = b1
    if remnant_block then
        blocks.insert(remnant_block_index, remnant_block)
    end
    return blocks
end

def find_file(blocks, file_id)
    blocks.reverse.each_index {
        |bi|
        if blocks[bi][0] == file_id then return bi end
    }
    return -1
end

def compress_memory_split_files(blocks)
    i = 0
    last_non_empty_block_index = blocks.length - 1
    while i < blocks.length - 1 do
        current_block = blocks[i]
        if current_block[0] == -1 then
            # Empty block, try to fill it
            last_non_empty_block = blocks[last_non_empty_block_index]
            swap_length = [last_non_empty_block[2], current_block[2]].min
            blocks = swap_blocks_partial(blocks, i, last_non_empty_block_index, swap_length)
            blocks = fuse_adjacent_blocks(blocks, blocks.length - 2)
            blocks = fuse_adjacent_blocks(blocks, i)
            last_non_empty_block_index = blocks.length - 2
        end
        i += 1
    end
    return blocks
end

def compress_memory_move_files(blocks)
    blocks.last[0].downto(0).each {
        |file_id|
        fi = find_file(blocks, file_id)
        blocks.each_index {
            |bi|
            if blocks[bi][0] == -1 && blocks[fi][1] > blocks[bi][1] && blocks[fi][2] <= blocks[bi][2] then
                # Empty space found for file, so we move it
                blocks = swap_blocks_partial(blocks, bi, fi, blocks[fi][2])
                blocks = fuse_adjacent_blocks(blocks, fi)
                blocks = fuse_adjacent_blocks(blocks, bi)
                break
            end
        }
    }
    return blocks
end

def get_checksum(blocks)
    sum = 0
    blocks.each {
        |block|
        if block[0] != -1 then
            sum += block[0] * (block[1]..block[1] + block[2] -1).sum
        end
    }
    return sum
end

# PART 1
def part1(input)
    file_system = get_file_system_representation(input)
    compressed_file_system = compress_memory_split_files(file_system)
    return get_checksum(compressed_file_system)
end

# PART 2
def part2(input)
    file_system = get_file_system_representation(input)
    compressed_file_system = compress_memory_move_files(file_system)
    return get_checksum(compressed_file_system)
end
