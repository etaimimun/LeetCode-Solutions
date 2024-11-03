class Solution {
public:

    int romanToInt(string s) {
   std::unordered_map<char, int> romanNums;
   romanNums['I'] = 1;
   romanNums['V'] = 5;
   romanNums['X'] = 10;
   romanNums['L'] = 50;
   romanNums['C'] = 100;
   romanNums['D'] = 500;
   romanNums['M'] = 1000;
   int currentSum = 0;

   char prevChar = 'p';
        for(char currentChar : s){
           if( (prevChar == 'I' && (currentChar == 'V' || currentChar == 'X')) ||
            (prevChar == 'X' && (currentChar == 'L' || currentChar == 'C')) ||
            (prevChar == 'C' && (currentChar == 'D' || currentChar == 'M')) ) {
                currentSum += (romanNums[currentChar] - 2*romanNums[prevChar]);
            } else {currentSum += romanNums[currentChar]; }
           
           prevChar = currentChar;
        }
    return currentSum;
    }
};