#include<iostream>
#include<bits/stdc++.h>
using namespace std;
char a[40]="A   3   HIL JM O   2TUVWXY51SE Z  8 ";

char fun(char m)
{
    if(m<='Z'&&m>='A')return a[m-'A'];
    else if(m<='9'&&m>='1')return a[m-'1'+26];
}

int main()
{
    char c[100],tr[100],p[100];
    //bool flag1=true,flag2=true,flag3=true;
    while(scanf("%s",c)!=EOF)
    {
        int len=strlen(c);
        for(int i=0;i<len;++i)
        {
            p[i]=c[len-1-i];
            tr[i]=fun(c[len-1-i]);
        }
        if(strcmp(c,p)!=0&&strcmp(c,tr)!=0)
        {
            printf("%s -- is not a palindrome.\n",c);
        }
        else if(strcmp(c,p)==0&&strcmp(c,tr)!=0)
        {
            printf("%s -- is a regular palindrome.\n",c);
        }
        else if(strcmp(c,p)!=0&&strcmp(c,tr)==0)
        {
            printf("%s -- is a mirrored string.\n",c);

        }
        else if(strcmp(c,p)==0&&strcmp(c,tr)==0)
        {
            printf("%s -- is a mirrored palindrome.\n",c);
        }
    }

    return 0;
}