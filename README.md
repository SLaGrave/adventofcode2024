# Advent of Code 2024

[Sam LaGrave](https://samlagrave.com/)'s Advent of Code (2024) submissions.

## Languages

As a self-professed "language nerd", I want to use Advent of Code to sharpen my skills in programming languages I don't use too much. I will likely do each day in Python 1st, since that's the language I'm most familiar with. After that, I may rewrite the day in a different language. I'll use this table to keep track.

<details>

<summary>My big tables of languages I've used each day (mostly Python)</summary>

| Day             | Title                  | Python              | Rust               | [Uiua](https://www.uiua.org) |
| --------------- | ---------------------- | ------------------- | ------------------ | ---------------------------- |
| [01](./day01/)  | Historian Hysteria     | :heavy_check_mark:  | :o:                | :heavy_check_mark:           |
| [02](./day02/)  | Red-Nosed Reports      | :heavy_check_mark:  | :o:                | :o:                          |
| [03](./day03/)  | Mull It Over           | :heavy_check_mark:  | :heavy_check_mark: | :o:                          |
| [04](./day04/)  | Ceres Search           | :heavy_check_mark:  | :o:                | :o:                          |
| [05](./day05/)  | Print Queue            | :heavy_check_mark:  | :o:                | :o:                          |
| [06](./day06/)  | Guard Gallivant        | :heavy_check_mark:  | :o:                | :o:                          |
| [07](./day07/)  | Bridge Repair          | :heavy_check_mark:  | :o:                | :o:                          |
| [08](./day08/)  | Resonant Collinearity  | :heavy_check_mark:  | :o:                | :o:                          |
| [09](./day09/)  | Disk Fragmenter        | :heavy_check_mark:  | :o:                | :o:                          |
| [10](./day10/)  | Hoof It                | :heavy_check_mark:  | :o:                | :o:                          |
| [11](./day11/)  | Plutonian Pebbles      | :heavy_check_mark:  | :o:                | :one:                        |
| [12](./day12/)  | Garden Groups          | :one:               | :o:                | :o:                          |
| [13](./day13/)  | Claw Contraption       | :heavy_check_mark:  | :o:                | :o:                          |
| [14](./day14/)  | Restroom Redoubt       | :heavy_check_mark:  | :o:                | :o:                          |
| [15](./day15/)  | Warehouse Woes         | :one:               | :o:                | :o:                          |
| [16](./day16/)  | Reindeer Maze          | :one:               | :o:                | :o:                          |
| [17](./day17/)  | Chronospatial Computer | :one:               | :o:                | :o:                          |
| [18](./day18/)  | RAM Run                | :heavy_check_mark:  | :o:                | :o:                          |
| [19](./day19/)  | Linen Layout           | :o:                 | :o:                | :o:                          |
| [20](./day20/)  | Race Condition         | :one:               | :o:                | :o:                          |


</details>

## Notes

- **Why I've done day 3 in Rust**
  - Each year, there is one problem that get's built upon over several puzzles. It's often a bytecode or language based puzzle. I expect it will be the memory system started today.
  - Because of this, I wanted to make a system that is more easily expandable.
  - I also just like [pest.rs](https://pest.rs) and wanted an excuse to use it.

- **I don't like my day 7 solution**
  - It takes just a second to run part 2.
  - Basically it grows 2^n (3^n in part 2) and I feel like there should be a way to make it better.

- **Day 14**
  - The second part is a little whack. It will generate a ton of images.
  - You can search manually, if you want...
  - Or just sort by size. PNG compression makes the tree the smallest image.
  - ![Day 14's tree](./8052.png)

- **Day 17**
  - Part two is long since I tried to brute forced it.
  - Restart code at: 1644410000
