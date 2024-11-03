class Solution {
public:
    int reverse(int x) {
        
        std::string numberAsString = std::to_string(x);
        
        std::string reversedNumber = "";
        bool is_negative = false;
     if(numberAsString[0] == '-') {  is_negative = true; }
        for(int currentNumber = numberAsString.length() - 1; currentNumber != -1; --currentNumber ){
            
            reversedNumber += numberAsString[currentNumber];
            
        }
  
        try {
        int reversedInt = std::stoi(reversedNumber);

        } catch (const std::out_of_range& e) {return 0;}
  

    if(is_negative) {return -1*(std::stoi(reversedNumber));}
        return std::stoi(reversedNumber);
    }
};