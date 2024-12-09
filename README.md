# Advent of Code 2024

[Sam LaGrave](https://samlagrave.com/)'s Advent of Code (2024) submissions.

## Languages

As a self-professed "language nerd", I want to use Advent of Code to sharpen my skills in programming languages I don't use too much. I will likely do each day in Python 1st, since that's the language I'm most familiar with. After that, I may rewrite the day in a different language. I'll use this table to keep track.

| Day             | Title                 | Python              | Rust               |
| --------------- | --------------------- | ------------------- | ------------------ |
| [01](./day01/)  | Historian Hysteria    | :heavy_check_mark:  | :o:                |
| [02](./day02/)  | Red-Nosed Reports     | :heavy_check_mark:  | :o:                |
| [03](./day03/)  | Mull It Over          | :heavy_check_mark:  | :heavy_check_mark: |
| [04](./day04/)  | Ceres Search          | :heavy_check_mark:  | :o:                |
| [05](./day05/)  | Print Queue           | :heavy_check_mark:  | :o:                |
| [06](./day06/)  | Guard Gallivant       | :heavy_check_mark:  | :o:                |
| [07](./day07/)  | Bridge Repair         | :heavy_check_mark:  | :o:                |
| [08](./day08/)  | Resonant Collinearity | :heavy_check_mark:  | :o:                |
| [09](./day09/)  | Disk Fragmenter       | :heavy_check_mark:  | :o:                |

## Notes

- **Why I've done day 3 in Rust**
  - Each year, there is one problem that get's built upon over several puzzles. It's often a bytecode or language based puzzle. I expect it will be the memory system started today.
  - Because of this, I wanted to make a system that is more easily expandable.
  - I also just like [pest.rs](https://pest.rs) and wanted an excuse to use it.

- **I don't like my day 7 solution**
  - It takes just a second to run part 2.
  - Basically it grows 2^n (3^n in part 2) and I feel like there should be a way to make it better.
