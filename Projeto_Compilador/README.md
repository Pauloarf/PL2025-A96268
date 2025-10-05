# Pascal Standard Compiler  

**A project to build a compiler for the standard Pascal language.**  

This project, part of the **Processamento de Linguagens 2025** course, focuses on developing a compiler capable of parsing, analyzing, and translating Pascal code into an intermediate representation or directly into machine code for the provided virtual machine.

---

## 🎯 Core Objectives
- **Lexical Analysis**: Convert Pascal source code into a list of tokens using `ply.lex`.  
- **Syntactic Analysis**: Validate code structure with a parser built using `ply.yacc`.  
- **Semantic Analysis**: Ensure type checking, variable declarations, and code consistency.  
- **Code Generation**:  
  - Generate an intermediate representation and traverse it to produce VM code.  
- **Testing**: Validate compiler correctness with sample Pascal programs.  

---

## 💡 Key Features
- **Full Pascal Support**: Variables, arithmetic expressions, control flow (`if`, `while`, `for`), and optional subprograms (`procedure` and `function`).  
- **Example Programs Supported**:  
  - Hello World  
  - Maximum of 3 numbers  
  - Factorial calculation  
  - Prime number verification  
  - Sum of an array  
  - Binary to decimal conversion (with and without a function)  

---

## 🛠️ Technology Stack
- **Language**: Python  
- **Lexical & Syntactic Tools**: `ply.lex`, `ply.yacc`  
- **Intermediate Representation**: Custom data structures  
- **Virtual Machine**: Provided by the course for code execution  

---

## 👥 Contributors
- Paulo Alexandre Rodrigues Ferreira  
- Alex Araújo Sá – [GitHub](https://github.com/alexaraujosa)  
- Rafael Santos Fernandes – [GitHub](https://github.com/DarkenLM)     

---

## 📚 Learning Outcomes
- Understanding of compiler design principles  
- Hands-on experience with lexical, syntactic, and semantic analysis  
- Code generation techniques and optional optimization  
- Testing and validating compiler correctness using multiple Pascal programs  

---

**Final Grade: 19/20**
