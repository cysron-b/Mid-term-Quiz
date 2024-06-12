**Question 1  **                                                                                                                                                                    100 pts

**Task Description:** Using any programming language you choose, Write a program that reads a list of integers from an input file. Generate an output file with a list of duplicate integers present in the input file.

**Instructions**
Download sample data for this assignment from this location Download location.
Read a file that has one integer on each line. The integer can be positive or negative.
5

14

5

-9

62

-1

-9

-9

For each input file in the sample data, you need to output a result file that contains a list of the Duplicate integers in this file. For example, in the sample data above, your result should be in the sample_results.txt file
The integers in the result file must be sorted in increasing order.
There must be one line in the result file for each Duplicate integer
For example, if the input is as shown in the bullet point above, the result must be:
-9

5

A few sample input and result files are given in the Sample data file for test purposes, and the files are in the link above.

Your code must also handle the following variations in the input file:

Integers in each line can have a white space before or after. A whitespace is limited to one or more tabs and space characters.
If there are any lines with no inputs or white spaces, those lines must be See example input files.
If there are any lines with two integers separated by white space, those lines must be skipped.
If any lines contain a non-integer input, those lines must be seen as an example input file.
Non-integer input includes alphabets, punctuation marks, non-numeric values, and floating point numbers.
Note:
The integers in the input file will range from -1023 to 1023.
You are not allowed to use built-in Libraries to implement this work; you are expected to implement your custom function to tackle the problem.
Feel free to implement your code locally before putting the final implementation in the textbox below. Ensure that your code runs appropriately before submitting; if your code fails to run correctly, you stand to lose points for correctness.

Happy Coding!!!


**Question 2**                                                                                                                                                                     100 pts

**Task Description:** 
Using any programming you choose, write a program that implements the instructions below:
A server logs IP Addresses in a file. Each line will have precisely one IP Address and the number of requests from that IP Address. An IP address can appear multiple times in the file. A manager must determine which IP addresses are making the maximum requests. The manager passes a variable “n” to your code and the log file. Generate an output file containing the top “n” IP addresses.

Download the sample data in this location;Download location;

To understand sample inputs and results, check the following files:
       a) sample_01_easy.log: This is the input file. Each line has an IP address and count of requests separated by a comma.

                   i) sample_01_easy_result_n3.txt: This is the result when the manager selects n=3. Each line has three values separated by commas. The first value is the                                        “importance” of the IP  address. The second value is the IP address. The third value has the total number of requests from this IP address.
                   ii) sample_01_easy_result_n4.txt: This is the result when the manager selects n=4. Notice that two entries have several requests of 20. These two are                                     considered “equally important”.
                   iii) sample_01_easy_result_n6.txt: This is the result when manager selects n=6. Notice that there are two entries having a number of requests as 20. These                              two are considered  “equally important”.
            b) sample_02_easy.log: This is the input file.
                    i) sample_01_easy_result_n3.txt: This is the result when manager selects n=3.
                    ii) sample_01_easy_result_n4.txt: This is the result when manager selects n=4.
                    iii) sample_01_easy_result_n6.txt: This is the result when manager selects n=6.
Note that the log files can be long, running into a few million lines. Each log file may contain requests from 100K or more IP addresses.
    You can assume there will be no variation in the input file format.
     In general, topN would be significantly smaller than the number of IP addresses.
 

Note on IP addresses that are equally important:
       a) If two IP addresses are equally important, ie. They have the same total count, then you should print them in increasing order of the IP address.
       b) For example, in sample_01_easy_result_n4.txt and sample_01_easy_result_n6.txt, the IP address 49.122.95.109 and 233.52.225.25 have same counts “20”. But                49.122.95.109 is printed before 233.52.225.25.
       c) Please see input file sample_03_easy.log and the result file sample_03_easy_result_n3.txt.

Here the IP address 192.168.10.5, 192.168.20.1, 192.168.10.3 had the same count (say 7) and importance (say 2), your code will print these as follows:
        2, 192.168.10.3, 7
        2, 192.168.10.5, 7
       2, 192.168.20.1, 7

 

Clues on implementation:
A trivial approach to solve this assignment is to create an array to store IP addresses and their counts. Once the file is parsed, search for the IP address with the topN counts. This method will consume too much memory and time once the log file becomes longer. In case of production log files that you may encounter in real-life/industrial implementations, this will simply fail.


An improved method would be to have two data structures:
1) Data structure to store count of IP addresses. As you parse the file, you will have to find out if an IP address has been seen before. If yes, its count will need to be incremented in this data structure. One can design nested linked lists, or hash tables for this data structure.
2) Data structure to store the “topN” IP addresses. This data structure should be an array containing “topN” elements. Each element in the array should be storing a list of IPAddresses that have this count. Note that when the count changes, the IP address would need to be removed from this list. A good data structure to use here is the Heap data structure with a size of topN. Count will be positive; it will be a good idea to use unsigned int to store counts. You may need to account for an extreme situation where the count of IP addresses may go beyond the limit imposed by unsigned int. This is not necessary for this assignment, but something you need to think about. Counting the topN occurrences is a normal requirement in modern web-based applications. The
counts can easily run into millions, if not more. A few practical use cases are below:
• Find out which search terms are most frequent today.
• Get the list of topics trending on social media.
• Get a list of hashtags that have the maximum number of re-tweets

Feel free to implement your code locally before putting the final implementation in the textbox below. Ensure that your code runs appropriately before submitting; if your code fails to run correctly, you stand to lose points for correctness.

Happy Coding!!!
