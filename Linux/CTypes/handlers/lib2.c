#include <stdio.h>
#include <threads.h>
#include <stdatomic.h>


atomic_int atomic_counter;
int non_atomic_counter;


int mythread(void* thr_data);
int start_thread();


int mythread(void* thr_data) {
    (void)thr_data;
    for(int n = 0; n < 1000; ++n) {
        ++non_atomic_counter;
        ++atomic_counter;
    }
    return 0;
}


int start_thread() {
    thrd_t thr[10];
    for(int n = 0; n < 10; ++n)
        thrd_create(&thr[n], mythread, NULL);
    for(int n = 0; n < 10; ++n)
        thrd_join(thr[n], NULL);
    printf("atomic     %d\n", atomic_counter);
    printf("non-atomic %d\n", non_atomic_counter);
    return 0;
}