use pest::Parser;
use pest_derive::Parser;

#[derive(Parser)]
#[grammar = "aoc.pest"]
pub struct InnerAOCParser;

#[derive(Debug)]
pub struct AOCParser {
    do_dont: bool,
}

impl AOCParser {
    pub fn new() -> Self {
        Self {
            do_dont: true,
        }
    }

    pub fn new_part1() -> Self {
        Self {
            do_dont: false,
        }
    }

    pub fn parse(&self, code: &str) {
        let successful_parse = InnerAOCParser::parse(Rule::aoc_program, code);
        println!("{:?}", successful_parse);
    }
}
