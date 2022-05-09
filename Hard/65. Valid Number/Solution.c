bool isNumber(char * s){
    int d = 1, n = 0, p=0, e=9999, ce=0;
    for (int i=0; i<strlen(s); i++){
        if (isdigit(s[i])) 
            n=1;
        if (s[i]=='.') 
            p++;
        if (s[i]=='-' || s[i]=='+'){
            if (i==strlen(s)-1) d=0;
            else if (i!=0){
                if (s[i-1]!='e')
                    d=0;
            }
        }
        else if (s[i]=='.'){
            if (i!=0){
                if (!isdigit(s[i-1]) && s[i-1]!='-' && s[i-1]!='+')
                    d=0;
            }
            else if (i!=strlen(s)-1){
                if (!isdigit(s[i+1]) && s[i+1]!='-' && s[i+1]!='+')
                    d=0;
            }
            if (i>e)
                d=0;
        }
        else if (!isdigit(s[i]) && s[i]!='-' && s[i]!='+' && s[i]!='e' && s[i]!='E' && s[i]!='.')
            d=0;
        else if (s[i]=='e' || s[i]=='E'){
            ce++;
            e=i;
            if (i==0 || i==strlen(s)-1) 
                d=0;
            else if (i!=0){
                if(!isdigit(s[i-1]) && s[i-1]!='.') 
                    d=0;
            }
            else if (i!=strlen(s)-1){
                if (!isdigit(s[i+1]) && s[i+1]!='+' && s[i+1]!='-')
                    d=0;
            }
        }
    }
    if (p>1 || ce>1) d=0;
    return d && n;
}