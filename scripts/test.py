import logging
import random
import string

# Configure logging
logging.basicConfig(filename='test.log', level=logging.INFO, format='%(asctime)s - %(message)s')

def generate_random_text(length):
    letters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(letters) for _ in range(length))

def main():
    for _ in range(100):  # Generate and log 1000 lines of random text
        random_text = generate_random_text(10)  # Each line has 100 characters
        logging.info(random_text)

if __name__ == "__main__":
    main()