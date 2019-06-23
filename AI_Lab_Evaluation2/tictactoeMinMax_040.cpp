#include<bits/stdc++.h>
using namespace std;


char computer = 'x', player = 'o',board [100][100];
int n;

struct Move
{
    int row, col;
};

bool movesPossible(char b[100][100])
{
    for (int i = 0; i<n; i++)
        for (int j = 0; j<n; j++)
            if (b[i][j]=='_')
                return true;
    return false;
}

int calculate(char b[100][100])
{

    for(int r=0; r<n; r++)
    {
        bool flag = true;
        for(int j=1; j<n; j++)
        {
            if(b[r][j]!=b[r][j-1])
            {
                flag = false;
                break;
            }
        }
        if(flag)
        {
            if (b[r][0]==computer)
                return +10;
            else if (b[r][0]==player)
                return -10;
        }
    }

    for(int c=0; c<n; c++)
    {
        bool flag = true;
        for(int i=1; i<n; i++)
        {
            if(b[i-1][c]!=b[i][c])
            {
                flag = false;
                break;
            }
        }
        if(flag)
        {
            if (b[0][c]==computer)
                return +10;
            else if (b[0][c]==player)
                return -10;
        }
    }

    bool flag = true;
    for(int i=1; i<n; i++)
    {
        if(b[i][i]!=b[0][0])
        {
            flag = false;
            break;
        }
    }
    if(flag)
    {
        if (b[0][0]==computer)
            return +10;
        else if (b[0][0]==player)
            return -10;
    }

    flag = true;
    for(int i=1; i<n; i++)
    {
        if(b[i][n-1-i] != b[0][n-1])
        {
            flag = false;
            break;
        }
    }
    if(flag)
    {
        if(b[0][n-1]==computer)
            return +10;
        else
            return -10;
    }


    return 0;
}

int minimax(char board[100][100], bool isComputer)
{
    int score = calculate(board);



    if (score == 10)
        return score;

    if (score == -10)
        return score;

    if (movesPossible(board)==false)
        return 0;

    if (isComputer)
    {
        int currentBest = -1000;

        for (int i = 0; i<n; i++)
        {
            for (int j = 0; j<n; j++)
            {

                if (board[i][j]=='_')
                {

                    board[i][j] = computer;

                    currentBest = max( currentBest,minimax(board, !isComputer) );

                    board[i][j] = '_';
                }
            }
        }
        return currentBest;
    }


    else
    {
        int currentBest = 1000;


        for (int i = 0; i<n; i++)
        {
            for (int j = 0; j<n; j++)
            {

                if (board[i][j]=='_')
                {

                    board[i][j] = player;

                    currentBest = min(currentBest,minimax(board, !isComputer));

                    board[i][j] = '_';
                }
            }
        }
        return currentBest;
    }
}

Move findBestMove(char board[100][100])
{

    int currentBest = -1000;
    Move bestMove;
    bestMove.row = -1;
    bestMove.col = -1;

    for (int i = 0; i<n; i++)
    {
        for (int j = 0; j<n; j++)
        {
            if (board[i][j]=='_')
            {
                board[i][j] = computer;

                int val = minimax(board, false);

                if (val > currentBest)
                {
                    bestMove.row = i;
                    bestMove.col = j;
                    currentBest = val;
                }


                board[i][j] = '_';
            }
        }
    }
    return bestMove;
}


bool printBoard(char b[100][100])
{
    for (int i = 0; i<n; i++)
    {
        for (int j = 0; j<n; j++)
        {
            cout<<b[i][j]<<" ";
        }
        cout<<endl;
    }
    cout<<endl;
}

int main()
{

    cout<<"Enter board size: ";
    cin>>n;

    for(int i=0; i<n; i++)
        for(int j=0; j<n; j++)
            board[i][j] = '_';

    bool isComputer = false;
    while(movesPossible(board) && calculate(board)!=10 && calculate(board)!=10)
    {
        if(isComputer)
        {

            Move bestMove = findBestMove(board);
            int r = bestMove.row;
            int c = bestMove.col;
            board[r][c] = 'x';
            cout<<"Computer Move: row "<<r+1<<", col "<<c+1<<endl;
            isComputer = false;
        }
        else
        {
            bool validMove = false;
            while(!validMove)
            {
                printBoard(board);
                int r,c;
                cout<<"Enter a move: "<<endl;
                cout<<"Enter row: ";
                cin>>r;
                cout<<"Enter column: ";
                cin>>c;

                if(r<0 || r>n || c<0 || c>n)
                    continue;

                r--;
                c--;
                if(board[r][c]=='_')
                {
                    cout<<"Your Move: row "<<r+1<<", col "<<c+1<<endl;

                    board[r][c] = 'o';

                    printBoard(board);

                    validMove = true;
                }
                else
                {
                    cout<<"Wrong Move!!! Try again..."<<endl;
                }

            }

            isComputer = true;

        }

    }

    cout<<"\n\tRESULT"<<endl;
    cout<<"    =============="<<endl<<endl;

    if(calculate(board)==10)
    {
        printBoard(board);
        cout<<"Computer Won"<<endl;
    }
    else if(calculate(board)==-10)
    {
        printBoard(board);
        cout<<"You Won "<<endl;
    }
    else
    {
        printBoard(board);
        cout<<"It's a tie!!!"<<endl;
    }
    return 0;
}

