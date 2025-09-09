# Agrichain SDET Assignment

Hi,  
This is the assignment done by **Aayush Garg** for the role of **SDET at Agrichain**.  

The repo contains two problems:

## Problem 1
Program to find the longest substring without repeating characters.  
- Written in **simple** and **advanced (sliding window)** way.  
- Manual test outputs included.  
- Automated unit test cases are also there.

## Problem 2
Automation test for a sample website (assumed locators since actual site not given).  
- Selenium test is created in `tests/test_problem2.py`.  
- Manual test cases written in markdown file.

---

### 🔹 How to Setup

1. Clone repo  
   ```bash
   git clone <your_repo_link>
   cd Agrichain-SDET-Assignment
   ```

2. Create virtual env and install packages  
   ```bash
   python -m venv venv
   source venv/bin/activate   # for mac/linux
   venv\Scripts\activate      # for windows

   pip install -r requirements.txt
   ```

3. Run manual code (Problem 1)  
   ```bash
   python problem1.py
   ```

4. Run automation unit tests  
   ```bash
   python -m unittest tests/test_problem1.py
   ```

5. Run selenium automation (Problem 2)  
   ```bash
   python -m unittest tests/test_problem2.py
   ```

---

✅ Everything is structured like a **real SDET repo** so recruiter can check logic, run tests and see automation skills.
