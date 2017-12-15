// Implement Stack Data Structure

#include<iostream>
void push(int);
void pop();
void show();
int stack[10] = {0,0,0,0,0,0,0,0,0,0}, top = -1;

using namespace std;

int main()
{
 int i;
 do
 {
  cout << "\n[1] Push";
  cout << "\n[2] Pop";
  cout << "\n[3] Show Stack";
  cout << "\n[0] Exit\n";
  cin >> i;
  if(i == 1)
  {
	int item;
	cout << "\nEnter New Value :\n";
  	cin >> item;
  	push(item);
  }
  else if(i == 2)
  {
	pop();
  }
  else if(i == 3)
  {
	show();
  }
 }while(i != 0);
}

void push(int i)
{
 if(top == 9)
 {
	cout << "\n**Stack Full**";
 }
 else
 {
	top++;
	stack[top] = i;
	cout << "\n**Item Pushed in the Stack**";
 }
}

void pop()
{
 if(top == -1)
 {
	cout << "\n**Stack Empty**";
 }
 else
 {
	stack[top] = 0;
	top--;
	cout << "\n**Item Popped**";
 }
}

void show()
{
 for(int i = 0; i < 10; i++)
 {
	cout << stack[i] << " ";
 }
 cout << "\nTop->" << top;
}
