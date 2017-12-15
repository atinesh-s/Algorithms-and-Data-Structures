// Implement Queue Data Structure

#include<iostream>
void enqueue(int);
void dequeue();
void show();
int queue[10] = {0,0,0,0,0,0,0,0,0,0}, front, rear;

using namespace std;

int main()
{
 int i;
 do
 {
  cout << "\n[1] Enqueue";
  cout << "\n[2] Dequeue";
  cout << "\n[3] Show Queue";
  cout << "\n[0] Exit\n";
  cin >> i;
  if(i == 1)
  {
	int item;
	cout << "\nEnter New Value :\n";
	cin >> item;
	enqueue(item);
  }
  else if(i == 2)
  {
	dequeue();
  }
  else if(i == 3)
  {
	show();
  }
 }while(i != 0);
}

void enqueue(int i)
{
 if((rear + 1) % 10 == front)
 {
	cout << "\n**Queue Full**";
 }
 else
 {
	queue[rear] = i;
	rear = (rear + 1) % 10;
	cout << "\n**Item Enqueued**";
 }
}

void dequeue()
{
 if(front == rear)
 {
	cout << "\n**Queue Empty**";
 }
 else
 {
	queue[front] = 0;
	front = (front + 1) % 10;
	cout << "\n**Item Dequeued**";
 }
}

void show()
{
 for(int i = 0; i < 10; i++)
 {
	cout << queue[i] << " ";
 }
 cout << "\nFront->" << front << ", Rear->" << rear;
}
