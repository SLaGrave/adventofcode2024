mod aoc_parser;

fn main() {
    let input = include_str!("../../input.txt");

    let part1 = aoc_parser::AOCParser::new_day3_part1();
    let part1_answer = part1.parse(input);
    println!("Part 1:\n{}", part1_answer);

    let part2 = aoc_parser::AOCParser::new();
    let part2_answer = part2.parse(input);
    println!("Part 2:\n{}", part2_answer);
}
