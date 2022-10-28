## Test projects

In tests folders are simple questions/tasks to solve.

### translate project

Translate folder contains training program which read data from inputs folder do some operation on data and
writes output to output folder.
The program has bug introduced, so first quest is to debug and run it.
It's intentionally created not pythonic, wrongly in some places.

Exercises:
 1. Run translate.py script with input.txt and output.txt files
 2. Fix exception
 3. Add logger DEBUG message which print each read line in TxtReader.read_element() method
 4. Raise exception when input file in Reader object cannot be found. File not exists
 5. Raise exception when output file in Writer object exists. File exists
 6. Correct program by removing redundant \n in value fields
 7. How to secure reader/writer factory against not exists reader/writer classes
 8. Add property to reader/writer class which returns full path to input/output file
 9. Allow writer.write() method to work also with tuple type, not only List[tuple] 
 10. Implement KeyValue(NamedTuple) class as return value from reader.read_element() method
 11. Implement KeyValue(NamedTuple) class as input value to writer.write() method
 12. Implement BinWriter class
 13. Why BinReader.read_element does not work when last character in input.bin file is #
 14. Refactor BinReader.read_element method. What should be done at first
 15. Implement conversion (convert to lowercase all characters in value field) as easy as possible 
 16. Implement conversion (convert to lowercase all characters in value field) without modifying main program
 17. Construct list comprehensions statement in writer.write() method

Questions:
1. What is abc - abstraction/interface class
2. Factory design patter
3. Context manager
4. Generator