/*开发一个简单错误记录功能小模块，能够记录出错的代码所在的文件名称和行号。
 
处理： 
 
1、 记录最多8条错误记录，循环记录，对相同的错误记录（净文件名称和行号完全匹配）只记录一条，错误计数增加；
 
2、 超过16个字符的文件名称，只记录文件的最后有效16个字符；
 
3、 输入的文件可能带路径，记录文件名称不能带路径。


输入描述:
一行或多行字符串。每行包括带路径文件名称，行号，以空格隔开。


输出描述:
将所有的记录统计并将结果输出，格式：文件名 代码行数 数目，一个空格隔开，如：

输入例子:
E:\V1R2\product\fpgadrive.c   1325

输出例子:
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

