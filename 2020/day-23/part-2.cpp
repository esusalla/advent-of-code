// Day 23, Part 2: Crab Cups

#include <iostream>

const long INP_LEN = 9;
const long LIMIT = 1000000;
const long ROUNDS = 10000000;

template <typename T>
class LList
{
public:
    struct Node {
        Node(const T& data = T(), Node* next = nullptr, Node* prev = nullptr) : data(data), next(next), prev(prev) {}
        T data;
        Node* next;
        Node* prev;
    };

    Node* head;
    Node* tail;

    LList() : head(nullptr), tail(nullptr) {}
    ~LList()
    {
        // Unlink
        if (head->prev) head->prev->next = nullptr;

        auto current = head;
        while (current) {
            head = head->next;
            delete current;
            current = head;
        }
    }

    Node* push_back(const T& data)
    {
        Node* node = new Node(data);

        if (!head) {
            head = node;
            tail = head;
        } else {
            tail->next = node;
            node->prev = tail;
            tail = node;
        }

        return node;
    }

    void connect()
    {
        head->prev = tail;
        tail->next = head;
    }
};

bool contains(long arr[], long size, long target)
{
    for (auto i = 0; i < size; ++i) {
        if (arr[i] == target) return true;
    }

    return false;
}

void shuffle(long& current, LList<long>& cups, LList<long>::Node* nodes[])
{
    auto rmv_start = nodes[current]->next;
    auto rmv_end = rmv_start;

    // Remove three cups after current cup
    long removed[3];
    for (auto i = 0; i < 3; ++i) {
        removed[i] = rmv_end->data;
        rmv_end = rmv_end->next;
    }
    rmv_end = rmv_end->prev;

    // Relink current cup to the cup following the last of the three removed
    nodes[current]->next = rmv_end->next;
    nodes[current]->next->prev = nodes[current];

    // Calculate insertion destination for removed cups by subtracting
    // from current cup until its value is not included in the removed cups.
    // Circle back to max cup upon reaching zero
    auto destination = current - 1 == 0 ? LIMIT : current - 1;
    while (contains(removed, 3, destination)) {
        destination = destination - 1 == 0 ? LIMIT : destination - 1;
    }

    // Reinsert the three removed cups after the destination cup and relink
    rmv_start->prev = nodes[destination];
    rmv_end->next = nodes[destination]->next;

    nodes[destination]->next->prev = rmv_end;
    nodes[destination]->next = rmv_start;

    // Set the next current cup to the one immediately after the current
    current = nodes[current]->next->data;
}

int main()
{
    long inp[] = {3, 6, 4, 2, 9, 7, 5, 8, 1};
    LList<long> cups;
    LList<long>::Node** nodes = new LList<long>::Node*[LIMIT + 1];

    // Insert input as array start
    for (auto i = 0; i < INP_LEN; ++i) {
        nodes[inp[i]] = cups.push_back(inp[i]);
    }

    // Fill rest of array with ascending numbers to limit
    for (auto i = INP_LEN + 1; i <= LIMIT; ++i) {
        nodes[i] = cups.push_back(i);
    }

    // Connect the head and tail of the array to make circular iterations easier
    cups.connect();

    auto current = cups.head->data;
    for (auto i = 0; i < ROUNDS; ++i) {
        shuffle(current, cups, nodes);
    }

    // Calculate product of two cups immediately following number one
    auto prod = nodes[1]->next->data * nodes[1]->next->next->data;
    std::cout << prod << std::endl;

    return 0;
}
