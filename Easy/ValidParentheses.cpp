class Solution {
public:
    bool isValid(string s) {
        std::stack<char> LastParentheses;
        
        for(int i = 0; i < s.length(); ++i) {
            if(s[i] == '(' || s[i] == '{' || s[i] == '[') {LastParentheses.push(s[i]);}
            if((s[i] == '}' || s[i] == ']' || s[i] == ')') && LastParentheses.empty()) {return false;}
            if(s[i] == '}' || s[i] == ']' || s[i] == ')') {
                if (s[i] == ')' && LastParentheses.top() != '(') {return false;}
                if (s[i] == ']' && LastParentheses.top() != '[') {return false;}
                if (s[i] == '}' && LastParentheses.top() != '{') {return false;}
                LastParentheses.pop();
            } 
           

        
    }
            if(!LastParentheses.empty()){return false;}
            return true;

    }
};