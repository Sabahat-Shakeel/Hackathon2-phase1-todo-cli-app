# 🚀 AI-Native Todo CLI App (Hackathon Phase 1)

## 📌 Overview  
- Python-based Todo CLI app built **AI-native**, using **Gemini CLI** + **Spec-Kit Plus** for fully automated, spec-driven development.

## 🧩 Core Features  
- ➕ Add tasks  
- 📝 Update tasks  
- ❌ Delete tasks  
- 📄 View tasks  
- ✔️ Mark tasks complete  
- ⚙️ In-memory storage  
- 🤖 Auto-generated modules via Gemini Code  
- 🧭 Spec-driven planning using `/sp.plan` & `/sp.implement`

## 🤖 AI-Native Development Workflow  
- 🟦 Write specifications in **Spec-Kit Plus**  
- 🟩 Generate code using **Gemini CLI**  
- 🔁 AI-guided spec → implement → test loop  
- 🧱 Stable file structure enforced automatically  
- 📜 Prompt history saved for reproducibility  

## 🛠 Tech Stack  
- 🐍 Python 3  
- 🔮 Gemini CLI (@google/geminicli)  
- 📘 Spec-Kit Plus (specifyplus)  
- 🧪 unittest for testing  

## 📂 Project Structure  
- `todo_app.py` → Main CLI application  
- `specs/` → Spec-Kit specifications  
- `tests/` → Test suite  
- `history/prompts/` → AI prompt logs  
- `.gemini/` & `.specify/` → Tool configs  


## 📥 Installation

### 📂 Enter Project
```bash
cd Hackathon2-phase1-todo-cli-app

## 🐍 Dont need to Install Python Dependencies manually
 ❌ pip install -r requirements.txt
 

## 🔮 Install Gemini CLI
npm install -g @google/geminicli

## 📘 Install Spec-Kit Plus
pip install specifyplus init <my-project> gemini

## 📥 Installation  
- Clone repo:  
  ```bash
  git clone https://github.com/Sabahat-Shakeel/Hackathon2-phase1-todo-cli-app
