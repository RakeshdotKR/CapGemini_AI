# For getting to know about interpreter
import sys

COURSE_NAME = "Python Fundamentals for GEN AI"

if __name__ == "__main__":
    print("="*50)
    print("Course:",COURSE_NAME)
    print("Python:", sys.version.split()[0])
    print("Platform:",sys.platform)
    print("="*50)
    day = 1
    print(f"Welcome to Day {day} of {COURSE_NAME}")
