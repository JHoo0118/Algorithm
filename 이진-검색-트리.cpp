// https://www.acmicpc.net/problem/5639

#include <iostream>

using namespace std;

struct Node
{
    int data;
    Node *left;
    Node *right;
};

class Tree
{
private:
    Node *head;

public:
    Tree() : head(nullptr) {}

    void Add(int data)
    {
        if (head == nullptr)
        {
            head = new Node({data, nullptr, nullptr});
            return;
        }
        AddNode(head, data);
    }

    void Print()
    {
        if (head == nullptr)
            return;
        PrintNode(head);
    }

private:
    // 후위 출력
    void PrintNode(Node *node)
    {
        if (node == nullptr)
            return;
        PrintNode(node->left);
        PrintNode(node->right);
        printf("%d\n", node->data);
    }

    void AddNode(Node *parent, int data)
    {
        if (parent->data > data)
        {
            if (parent->left == nullptr)
                parent->left = new Node({data, nullptr, nullptr});
            else
                AddNode(parent->left, data);
        }
        else
        {
            if (parent->right == nullptr)
                parent->right = new Node({data, nullptr, nullptr});
            else
                AddNode(parent->right, data);
        }
    }
};

int main()
{
    Tree t;
    int input;
    while (cin >> input)
        t.Add(input);
    t.Print();
    return 0;
}