class SuperStoneSolver
    # With its power of prediction, the SuperStoneSolver3000™ will trivialize your stone counting
    attr_accessor :stone_knowledge

    def initialize()
        @stone_knowledge = Array.new(100) {Hash.new}
    end

    def process_stone_count(stone, remaining_steps)
        return 1 if remaining_steps == 0

        # If count already computed, return it
        return @stone_knowledge[remaining_steps][stone] if @stone_knowledge[remaining_steps][stone]

        # Else, compute it and store it
        new_stones = nil
        if stone == "0" then
            new_stones=  ["1"]
        elsif stone.length % 2 == 0 then
            new_stones = [stone[0, stone.length / 2], Integer(stone[stone.length / 2, stone.length] , 10).to_s]
        else
            new_stones = [(Integer(stone, 10) * 2024).to_s]
        end

        count = 0
        for s in new_stones do
            count += self.process_stone_count(s, remaining_steps - 1)
        end
        @stone_knowledge[remaining_steps][stone] = count
        return count
    end

    def process_stones(stones, total_steps)
        count = 0
        for stone in stones do
            count += self.process_stone_count(stone, total_steps)
        end
        return count
    end
end