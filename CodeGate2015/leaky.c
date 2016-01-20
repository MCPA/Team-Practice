#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>
#include <fcntl.h>


char buf[80];

int main (int argc, char **argv)
{
  unsigned int filler0 = ???;
  unsigned int filler1 = ???;
  unsigned int filler2 = ???;
  unsigned int filler3 = ???;
  unsigned int key = ???;
  unsigned int filler4 = ???;
  unsigned int filler5 = ???;
  unsigned int filler6 = ???;
  unsigned int filler7 = ???;
  unsigned int filler8 = ???;

  unsigned int red = read(STDIN_FILENO,buf,80);
  buf[red] = '\x00';
  printf(buf);
}
