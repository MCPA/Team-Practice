#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <unistd.h>

struct record {
   char name[20];
   char rank[2];
   int id;
};

struct link {
   struct record data;
   struct link* next;
};


void print_records (struct link *);
void add_record(struct link** );
void delete_record(struct link** );

int main() {
   int option; struct link *record_list=NULL;
   while(1) {
      printf("\nPlease enter '1' to list personnel records, '2' to add a record, '3' to delete a record by ID, or any other number to exit: ");
      scanf("%d", &option);
      switch (option){
         case 1:  print_records(record_list); break;
         case 2:  add_record(&record_list); break;
         case 3:  delete_record(&record_list); break;
	 default: {
            struct link* i = record_list;
            struct link* p;
            while (i->next != record_list){
               p = i;
               i = i->next;
               free(p);
            } 
            free(i);
            return 0;
            }
      sleep(2);
      } 
}
}

void print_records(struct link* record_list){
   if (record_list == NULL) {
      printf ("\nNo records to print!\n");
      return;
   }

   struct link* i = record_list;
   do {
   printf("\nName: %s\n", i->data.name);
   printf("Rank: %s\n", i->data.rank);
   printf("ID: %d\n", i->data.id);
   i = i->next;
   } while (i != record_list);
}

void add_record(struct link **record_list){
   struct link *new_record=(struct link*)malloc(sizeof(struct link));
   printf("\nEnter person's name: ");
   scanf("%s", new_record->data.name);
   printf("\nEnter person's rank (2 characters): ");
   scanf("%s", new_record->data.rank);
   printf("\nEnter person's ID: ");
   scanf("%d", &new_record->data.id);

   if (*record_list == NULL) {
      *record_list = new_record;
      new_record->next = *record_list;
      return;
   }

   struct link* i = *record_list;
   while(i->next != *record_list)  
     i = i->next;
     if (i->next == *record_list) {
        new_record->next = *record_list;
        i->next = new_record;
     } 
    
}

void delete_record(struct link **record_list){
   int del_id;
   struct link* i = *record_list;
   struct link* p;
   printf("\nEnter ID of record to delete: ");
   scanf("%d", &del_id);
   do {
      if (i->next->data.id == del_id) {
         p = i->next->next;
         if (i->next == *record_list)
            *record_list = p;
         free(i->next); 
         i->next = p;
         break;
      }
      i = i->next;
   } while (i != *record_list);
}
