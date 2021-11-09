# How to Run The Program
1. Navigate to directory containing the python script and .meta, .train, and.test files
2. Type `python3 naivebayes.py` into the terminal
3. Follow the instructions as given by the program:
- Option 1. Read in new meta data file and training file to train model
- Option 2. Read in a test file and and calculate accuracy
- Option 3. Read in a data file and classify the data
- Option 4. Exit the program

# How it Works
The program works by :
- Taking a .meta file which describes the data and classifications
- Reading a training file and training the model based on the description of the data in the .meta file
- Testing the file one a test file with given classificaitions for comparison with those produced by the model
- Classifying the items on a file given either labeless or labeled