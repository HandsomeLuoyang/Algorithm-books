#include <iostream>
#include <string>
using namespace std;

struct ListNode
{
    int val;
    ListNode *next;
    ListNode(int x) : val(x), next(NULL) {}
};

class Solution
{
public:
    ListNode *removeNthFromEnd(ListNode *head, int n)
    {
        ListNode *left_node = head;
        ListNode *right_node = head;
        for (int i = 0; i < n - 1; i++)
        {
            right_node = right_node->next;
        }
        if (!right_node->next)
        {
            return head->next;
        }

        ListNode *tmp_node = NULL;
        while (right_node->next)
        {
            tmp_node = left_node;
            left_node = left_node->next;
            right_node = right_node->next;
        }
        tmp_node->next = left_node->next;
        return head;
    }
};

int main()
{
    return 0;
}