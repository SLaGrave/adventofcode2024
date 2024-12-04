use pest::Parser;
use pest_derive::Parser;

#[derive(Parser)]
#[grammar = "aoc.pest"]
pub struct PestParser;

pub struct AOCParser {
    do_dont: bool,
    enabled: bool,
    total: i32,
}

impl AOCParser {
    pub fn new() -> Self {
        Self {
            do_dont: true,
            enabled: true,
            total: 0,
        }
    }

    pub fn new_day3_part1() -> Self {
        Self {
            do_dont: false,
            enabled: true,
            total: 0,
        }
    }

    pub fn get_total(&self) -> i32 {
        self.total
    }

    pub fn parse(mut self, code: &str) -> i32 {
        let program = PestParser::parse(Rule::aoc_program, code)
            .expect("Unsuccessful parse")
            .next()
            .unwrap();
        for item in program.into_inner() {
            match item.as_rule() {
                Rule::aoc_mul => {
                    if self.enabled {
                        // Parse lhs & rhs
                        // We're happen to trust that there can ONLY be
                        // EXACTLY two ints here, if Pest did it's job.
                        let mut values: Vec<i32> = vec![];
                        for value in item.into_inner() {
                            let v = str::parse::<i32>(value.as_span().as_str()).unwrap();
                            values.push(v);
                        }
                        // Multiply them together
                        // and add to total
                        self.total += values.get(0).unwrap() * values.get(1).unwrap()
                    }
                }
                Rule::aoc_do => {
                    if self.do_dont {
                        self.enabled = true;
                    }
                }
                Rule::aoc_dont => {
                    if self.do_dont {
                        self.enabled = false;
                    }
                }
                _ => unreachable!(),
            }
        }
        self.get_total()
    }
}
