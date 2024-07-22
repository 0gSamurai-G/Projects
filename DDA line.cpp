// C++ program for DDA line generation 
  
#include <bits/stdc++.h> 
#include <graphics.h> 
#include <math.h> 
#include <stdio.h>
using namespace std; 

int round(float n){
	if ((n-(int) n) < 0.5){
		return (int)n;
	}
	else{
		return (int) n+1;
	}
	
}

void DDALine(int x1,int y1,int x2,int y2){
	int dx=x2-x1;
	int dy=y2-y1;
	
	int step;
	
	if (abs(dx)>abs(dy)){
		step=abs(dx);
	}
	else{
		step=abs(dy);
	}
	
	float xinc= (float)dx/step;
	float yinc= (float)dy/step;
	
	float x=x1;
	float y=y1;
	
	for (int i=0;i<=step;i++){
		
		putpixel(round(x), round(y), YELLOW);
		x+=xinc;
		y+=yinc;
		
		
	}
}

int main(){
	int gd = DETECT, gm;
	initgraph(&gd,&gm,"");
	int x1,y1,x2,y2;
	DDALine(100,100,500,100);
	getch();
	
	return 0;
}