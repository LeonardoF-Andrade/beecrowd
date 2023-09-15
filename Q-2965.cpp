#include <iostream>
#include <vector>
#include <algorithm>

using namespace std;

class Grafo {
public:
    int vertices;
    int height;
    int descen;
    bool use;

    Grafo(int v) : vertices(v), height(-1), descen(-1), use(false) {}

    void Set(int h, int idi) {
        height = h;
        descen = idi;
    }

    bool GetUse() const {
        return use;
    }

    void SetUse() {
        use = true;
    }

    int GetHei() const {
        return height;
    }

    int Getdes() const {
        return descen;
    }
};

int folha = 0;
int N, K, R = 0;

int Height(vector<vector<Grafo>>& list, int idi) {
    vector<pair<int, int>> Path = {{0, -1}};
    for (int i = 1; i < list[idi].size(); i++) {
        int id = list[idi][i].vertices;
        Path.push_back({Height(list, id) + 1, id});
    }
    imprimirGrafo(Path);
    pair<int, int> Max = *max_element(Path.begin(), Path.end());
    list[idi][0].Set(Max.first + 1, Max.second);
    if (list[idi][0].descen == -1) {
        folha++;
    }
    return Max.first;
}

void resp(vector<vector<Grafo>>& lista, int li, int j) {
    if (!lista[li][0].GetUse()) {
        R++;
        lista[li][0].SetUse();
        if (lista[li][0].descen == -1) {
            return;
        }
        for (int i = j; i < N; i++) {
            if (lista[i][0].vertices == lista[li][0].descen) {
                break;
            }
        }
        resp(lista, li, j + li);
    }
}
void imprimirGrafo(const vector<vector<Grafo>>& List) {
    for (int i = 1; i < List.size(); i++) {
        cout << "Vertice " << i << ": ";
        for (int j = 1; j < List[i].size(); j++) {
            cout << "(" << List[i][j].vertices << ", " << List[i][j].height << ", " << List[i][j].descen << ", " << List[i][j].use << ") ";
        }
        cout << endl;
    }
}

int main() {
    cin >> N >> K;
    vector<vector<Grafo>> List(N + 1, vector<Grafo>(1, Grafo(0)));

    for (int i = 2; i <= N; i++) {
        int v;
        cin >> v;
        List[v].push_back(Grafo(i));
    }
    
   // imprimirGrafo(List);
    Height(List, 1);
   // imprimirGrafo(List);
    if (folha <= K) {
        cout << N << endl;
    } else {
        sort(List.begin(), List.end(), [](const vector<Grafo>& a, const vector<Grafo>& b) {
            return a[0].GetHei() > b[0].GetHei();
        });

        int cont = 0;
        for (int i = 0; i < N; i++) {
            if (!List[i][0].GetUse()) {
                if (cont == K - 1) {
                    cont++;
                    R += List[i][0].GetHei();
                } else {
                    resp(List, i, i);
                    cont++;
                }
            }
            if (cont == K) {
                break;
            }
        }
        imprimirGrafo(List);
        cout << R << endl;
    }

    return 0;
}
