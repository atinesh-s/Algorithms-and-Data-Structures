// Implement Depth First Search (DFS) Algorithm

// Enter pair of vertices for an Edge (v1,v2) or (v2,v1))

// Don't I/P disconnected graph, Otherwise the result will not be as expected.

// Choose vertices as integers 0,1,2,..., SIZE-1 in any order.

// All arrays should be initialized to 0 for correct result(Some compiler implicitly initialized all the arrays to 0, Some doesn't).

#include<iostream>
#define SIZE 7
#define SOURCE 4
void push(int);
int pop();
void DFS();
int stack[SIZE], visited[SIZE], dfs_order[SIZE], k = 0, top = -1, m;
int graph[SIZE][SIZE];

using namespace std;

int main()
{
 int t, v1, v2;
 do
 {
  cout << "\n[1] Enter an Edge of the graph";
  cout << "\n[0] Exit and compute DFS order\n";
  cin >> t;
  if(t == 1)
  {
   cout << "\nEnter 1st Vertex of an Edge:\n";
   cin >> v1;
   cout << "\nEnter 2n Vertex of an Edge:\n";
   cin >> v2;
   graph[v1][v2] = 1;
   graph[v2][v1] = 1;
  }
 }while(t!=0);

 push(SOURCE);
 visited[SOURCE] = 1;
 dfs_order[k] = SOURCE;
 k++;

 while(top != -1)
 {
  DFS();
 }
 cout << "\nOne of the DFS order :\n";
 for(int i = 0; i < SIZE; i++)
 {
  cout << dfs_order[i];
 }
 cin >> m;
}

void push(int i)
{
 top++;
 stack[top] = i;
}

int pop()
{
 int t = stack[top];
 stack[top] = 0;
 top--;
 return t;
}

void DFS()
{
 int t;
 t = pop();

 for(int i = 0; i<SIZE; i++)
 {
  if(graph[t][i] == 1 && visited[i] != 1)
  {
   push(i);
   visited[i] = 1;
   dfs_order[k] = i;
   k++;
   break;
  }
 }
}
