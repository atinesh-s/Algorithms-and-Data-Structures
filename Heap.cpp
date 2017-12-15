// Implement heap Data Structure

#include<iostream>
#include<math.h>
# define SIZE 10
int extract_max();
int increase_key(int, int);
void insert(int);
void heapify(int);
int heap[SIZE];
int CS = 0; //Current Size

using namespace std;

int main()
{
 int i;
 do
 {
     cout << "\n[1] Extract Max";
     cout << "\n[2] Increase Key";
     cout << "\n[3] Insert";
     cout << "\n[4] Show Heap";
     cout << "\n[0] Exit\n";
     cin >> i;

     if(i == 1)
     {
        if(CS != 0)
        {
            int t;
            t = extract_max();
            cout << "\nMaximum Value : " << t;
        }
        else
        {
            cout << "\nHeap is Empty";
        }
     }
     else if(i == 2)
     {
        int t1, t2;
        cout << "\nEnter the position of the key to be Increased :\n";
        cin >> t1;
        cout << "\nEnter the new Increased Value :\n";
        cin >> t2;
        int r = increase_key(t1, t2);
        if(r != 0)
        {
            cout << "\nKey Value Increased";
        }
     }
     else if(i == 3)
     {
        int k;
        cout << "\nPlease Enter the new Key :\n";
        cin >> k;
        insert(k);
     }
     else if(i == 4)
     {
        for(int i = 0; i < CS; i++)
        {
            cout << heap[i] << " ";
        }
     }
 }while(i != 0);
}
int extract_max()
{
    int t;
    t = heap[0];
    heap[0] = heap[CS - 1];
    CS--;
    heapify(0);
    return t;
}
int increase_key(int i, int k)
{
    int r = 1;
    if(heap[i] < k)
    {
        heap[i] = k;
        while(i > 0)
        {
            int p = floor((i-1)/2); //Parent of i
            if(heap[p] < heap[i])
            {
                int t;
                t = heap[p];
                heap[p] = heap[i];
                heap[i] = t;
                i = p;
            }
            else
            {
                break;
            }
        }
    }
    else
    {
        cout << "\nNew key is smaller than the Current key";
        r = 0;
    }
    return r;
}
void insert(int k)
{
    CS++;
    if(CS <= SIZE)
    {
        increase_key(CS - 1, k);
        cout << "\nValue Inserted";
    }
    else
    {
       cout << "\nHeap is Full";
    }
}

void heapify(int i)
{
    int l,r, largest;
    l = 2 * i + 1;
    r = 2 * i + 2;
    if(l < CS || r < CS)
    {
        if(heap[l] > heap[r])
        {
            largest = l;
        }
        else
        {
            largest = r;
        }

        if(heap[largest] > heap[i])
        {
            int t;
            t = heap[largest];
            heap[largest] = heap[i];
            heap[i] = t;
            i = largest;
            heapify(i);
        }
    }
}
