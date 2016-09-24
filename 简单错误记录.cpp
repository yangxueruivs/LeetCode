/*����һ���򵥴����¼����Сģ�飬�ܹ���¼����Ĵ������ڵ��ļ����ƺ��кš�
 
���� 
 
1�� ��¼���8�������¼��ѭ����¼������ͬ�Ĵ����¼�����ļ����ƺ��к���ȫƥ�䣩ֻ��¼һ��������������ӣ�
 
2�� ����16���ַ����ļ����ƣ�ֻ��¼�ļ��������Ч16���ַ���
 
3�� ������ļ����ܴ�·������¼�ļ����Ʋ��ܴ�·����


��������:
һ�л�����ַ�����ÿ�а�����·���ļ����ƣ��кţ��Կո������


�������:
�����еļ�¼ͳ�Ʋ�������������ʽ���ļ��� �������� ��Ŀ��һ���ո�������磺

��������:
E:\V1R2\product\fpgadrive.c   1325

�������:
fpgadrive.c 1325 1
*/
#include<iostream>
#include<string>
#include<algorithm>
#include<vector>
#include<map>
#include<queue>

using namespace std;

string real_name(string str){
	return str.substr(str.rfind('\\')+1);
}

int main(){
	string path;
	int lines, count=0;
	map <pair<string, int>, int> error_files;
	queue <pair<string, int> > que;
	while(cin>>path>>lines){
		path = real_name(path);
		if(error_files.find(make_pair(path,lines))==error_files.end()){
			error_files[make_pair(path,lines)] = 1;
			if(que.size()<8)
				que.push(make_pair(path,lines));
			else{
				que.pop();
				que.push(make_pair(path,lines));
			}
		}
		else
			error_files[make_pair(path,lines)]++;
	}
	while(!que.empty()){
		if(que.front().first.size()>16)
			cout<<que.front().first.substr(que.front().first.size()-16)<<" "<<que.front().second<<" "<<error_files[que.front()]<<endl;
		else
			cout<<que.front().first<<" "<<que.front().second<<" "<<error_files[que.front()]<<endl;
		que.pop();
	}
	return 0;
}

