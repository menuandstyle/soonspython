#include<iostream>
using namespace std;

int main()
{
	cout << "201511190 ���ȯ" << endl;


	const int row = 4;
	const int col = 5;
	int count = 0;
	int num1;
	char num2;
	bool seat[row][col] = {};
	while (1)
	{
		for (int i = 0; i < row; i++)
		{
			cout << i << " :\t";
			for (int j = 0; j < col; j++)
			{
				if (seat[i][j] == 1)
					cout << "����\t";
				else
					cout <<(char)(j+65) <<"\t";
			}
			cout << endl;
		}
		cout << "============================================================" << endl;
		cout << "������ �� �¼��� �Է� �ϼ���(ex:1 C) :";
		cin >> num1 >> num2;
		if (seat[num1][(int)(num2 - 65)])
			cout << "�̹� ���� �Ǿ���" << endl;
		else
		{
			seat[num1][(int)(num2 - 65)] = true;
			count++;
		}
		if(count == (row*col))
			{
				cout << "�� �¼��� ���� �Ϸ��!!!!!!!" << endl;
				break;
			}
	}

	return 0;
}