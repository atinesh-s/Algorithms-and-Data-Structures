// Implement Breadth First Search (BFS) Algorithm

// Enter pair of vertices for an Edge (v1,v2) or (v2,v1))

// Don't I/P disconnected graph, Otherwise the result will not be as expected.

// Choose vertices as integers 0,1,2,..., SIZE-1 in any order.

// All arrays should be initialized to 0 for correct result(Some compiler implicitly initialized all the arrays to 0, Some doesn't).

#include<iostream>
#define SIZE 7
#define SOURCE 1
void enqueue(int);
int dequeue();
void BFS();
int queue[SIZE], visited[SIZE], bfs_order[SIZE], k = 0, front = 0, rear = 0, m;
int graph[SIZE][SIZE];

using namespace std;

int main()
{
 int t, v1, v2;
 do
 {
  cout << "\n[1] Enter an Edge of the graph";
  cout << "\n[0] Exit and compute BFS order\n";
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
 }while(t != 0);

 enqueue(SOURCE);
 visited[SOURCE] = 1;

 while(front != rear)
 {
  BFS();
 }
 cout << "\nOne of the BFS order :\n";
 for(int i = 0; i < SIZE ;i++)
 {
  cout << bfs_order[i];
 }
 cin >> m;
}

void enqueue(int i)
{
 queue[rear] = i;
 rear = rear + 1;
}

int dequeue()
{
 int t = queue[front];
 queue[front] = 0;
 front = front + 1;
 return t;
}

void BFS()
{
 int t;
 t = dequeue();
 bfs_order[k] = t;
 k++;
 for(int i = 0; i < SIZE; i++)
 {
  if(graph[t][i] == 1 && visited[i] != 1)
  {
   enqueue(i);
   visited[i] = 1;
  }
 }
}
