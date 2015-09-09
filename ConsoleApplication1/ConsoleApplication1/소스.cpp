#include<iostream>
using namespace std;

int main()
{
	cout << "201511190 목승환" << endl;


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
					cout << "있음\t";
				else
					cout <<(char)(j+65) <<"\t";
			}
			cout << endl;
		}
		cout << "============================================================" << endl;
		cout << "예약을 할 좌석을 입력 하세요(ex:1 C) :";
		cin >> num1 >> num2;
		if (seat[num1][(int)(num2 - 65)])
			cout << "이미 예약 되었음" << endl;
		else
		{
			seat[num1][(int)(num2 - 65)] = true;
			count++;
		}
		if(count == (row*col))
			{
				cout << "전 좌석이 예약 완료됨!!!!!!!" << endl;
				break;
			}
	}

	return 0;
}