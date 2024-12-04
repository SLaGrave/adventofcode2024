mod aoc_parser;

fn main() {
    let part1 = aoc_parser::AOCParser::new_part1();
    part1.parse("mul(12,165)asdad");

    let part2 = aoc_parser::AOCParser::new();
    part2.parse("mul(12,165)asdad");
}
