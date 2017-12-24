#[derive(Debug, Clone)]
enum Instruction {
    Set(String, String),
    Sub(String, String),
    Mul(String, String),
    Jnz(String, String),
}

impl Instruction {
    fn from_line(line: &str) -> Self {
        let mut parts = line.split_whitespace();

        let mnemonic = parts.next().expect("Could not find mnemonic.");
        let x = parts.next().expect("Could not find X.");
        let y = parts.next().expect("Could not find Y.");

        match mnemonic {
            "set" => Instruction::Set(x.to_owned(), y.to_owned()),
            "sub" => Instruction::Sub(x.to_owned(), y.to_owned()),
            "mul" => Instruction::Mul(x.to_owned(), y.to_owned()),
            "jnz" => Instruction::Jnz(x.to_owned(), y.to_owned()),
            _     => panic!("Unknown mnemonic {:?} (args were {:?} and {:?})", mnemonic, x, y),
        }
    }
}

struct CPU {
    registers: [isize; 8],
    code: Vec<Instruction>,

    pc: usize,
}

impl CPU {
    fn new(code: Vec<Instruction>) -> Self {
        Self {
            registers: [0; 8],
            code: code,

            pc: 0,
        }
    }

    fn optimize(&mut self) {

    }

    fn compute_value(&self, argument: &str) -> isize {
        if let Ok(n) = argument.parse() {
            n
        } else if argument.len() == 1 {
            let register = argument.chars().next().unwrap();

            self.registers[(register as usize) - ('a' as usize)]
        } else {
            panic!("Could not compute value of {:?}", argument);
        }
    }

    fn set_register(&mut self, register: &str, value: isize) {
        if register.len() != 1 {
            panic!("Tried to set invalid register {:?}", register);
        }

        let register = register.chars().next().unwrap();

        self.registers[(register as usize) - ('a' as usize)] = value;
    }

    fn execute_instruction(&mut self) -> bool {
        if self.pc >= self.code.len() {
            return false;
        }

        match self.code[self.pc].clone() {
            Instruction::Set(ref x, ref y) => {
                let y_value = self.compute_value(y);
                self.set_register(x, y_value);
                self.pc += 1;
            },

            Instruction::Sub(ref x, ref y) => {
                let x_value = self.compute_value(x);
                let y_value = self.compute_value(y);

                self.set_register(x, x_value - y_value);
                self.pc += 1;
            },

            Instruction::Mul(ref x, ref y) => {
                let x_value = self.compute_value(x);
                let y_value = self.compute_value(y);

                self.set_register(x, x_value * y_value);
                self.pc += 1;
            },

            Instruction::Jnz(ref x, ref y) => {
                if self.compute_value(x) == 0 {
                    self.pc += 1;
                } else {
                    self.pc = ((self.pc as isize) + self.compute_value(y)) as usize;
                }
            },
        }

        true
    }
}

fn main() {
    let code = include_str!("input.txt").lines()
                                        .map(Instruction::from_line)
                                        .collect();
    let mut cpu = CPU::new(code);
    cpu.registers[0] = 1;
    cpu.optimize();

    while cpu.execute_instruction() {}

    println!("{}", cpu.registers[7]);
}
