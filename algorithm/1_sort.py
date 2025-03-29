import time  # 引入 time 模块
import random  # 引入 random 模块

# 时间复杂度 O(n^2) 级排序算法
# 冒泡排序、选择排序、插入排序
class Sort_Algorithm_O_n2:
    """
    时间复杂度 O(n^2) 级排序算法
    包含冒泡排序、选择排序、插入排序
    """
    # 冒泡排序
    def bubble_sort(arr):
        """
        使用冒泡排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        print("冒泡排序")
        n = len(arr)  # 获取数组长度
        for i in range(n):
            for j in range(0, n-i-1):
                if arr[j] > arr[j+1]:  # 如果当前元素大于下一个元素，则交换它们
                    arr[j], arr[j+1] = arr[j+1], arr[j]
            print(f"{arr}")  # 打印当前排序状态
        return arr

    # 选择排序
    def selection_sort(arr):
        """
        使用选择排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        print("选择排序")
        n = len(arr)  # 获取数组长度
        for i in range(n):
            min_idx = i  # 假设当前元素为最小值
            for j in range(i+1, n):
                if arr[j] < arr[min_idx]:  # 找到更小的元素
                    min_idx = j
            arr[i], arr[min_idx] = arr[min_idx], arr[i]  # 交换当前元素和最小值
            print(f"{arr}")  # 打印当前排序状态
        return arr

    # 插入排序
    def insertion_sort(arr):
        """
        使用插入排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        print("插入排序")
        for i in range(1, len(arr)):
            key = arr[i]  # 当前元素
            j = i - 1
            while j >= 0 and key < arr[j]:  # 找到合适的位置插入当前元素
                arr[j + 1] = arr[j]
                j -= 1
            arr[j + 1] = key  # 插入当前元素
            print(f"{arr}")  # 打印当前排序状态
        return arr

# 时间复杂度 O(nlogn) 级排序算法
# 快速排序、堆排序、希尔排序、归并排序
class Sort_Algorithm_O_nlogn:
    
    # 快速排序
    def quicksort(arr):
        """
        使用快速排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        # print("快速排序")
        if len(arr) <= 1:
            return arr
        pivot = arr[len(arr) // 2]  # 选择中间元素作为基准
        left = [x for x in arr if x < pivot]  # 小于基准的元素
        middle = [x for x in arr if x == pivot]  # 等于基准的元素
        right = [x for x in arr if x > pivot]  # 大于基准的元素
        end = Sort_Algorithm_O_nlogn.quicksort(left) + middle + Sort_Algorithm_O_nlogn.quicksort(right)
        print(f"{end}")  # 打印当前排序状态
        return end
    
    # 堆排序
    def heapsort(arr):
        """
        使用堆排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        print("堆排序")
        def heapify(arr, n, i):
            largest = i
            left = 2 * i + 1
            right = 2 * i + 2
            if left < n and arr[left] > arr[largest]:
                largest = left
            if right < n and arr[right] > arr[largest]:
                largest = right
            if largest != i:
                arr[i], arr[largest] = arr[largest], arr[i]
                heapify(arr, n, largest)
        n = len(arr)
        for i in range(n // 2 - 1, -1, -1):
            heapify(arr, n, i)
        for i in range(n - 1, 0, -1):
            arr[i], arr[0] = arr[0], arr[i]
            heapify(arr, i, 0)
            print(f"{arr}")
        return arr
    
    # 希尔排序
    def shellsort(arr):
        """
        使用希尔排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        print("希尔排序")
        n = len(arr)
        gap = n // 2
        while gap > 0:
            for i in range(gap, n):
                temp = arr[i]
                j = i
                while j >= gap and arr[j - gap] > temp:
                    arr[j] = arr[j - gap]
                    j -= gap
                arr[j] = temp
            gap //= 2
            print(f"{arr}")
        return arr
    
    # 归并排序
    def mergesort(arr):
        """
        使用归并排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        print("归并排序")
        if len(arr) > 1:
            mid = len(arr) // 2
            left = arr[:mid:]
            right = arr[mid:]
            Sort_Algorithm_O_nlogn.mergesort(left)
            Sort_Algorithm_O_nlogn.mergesort(right)
            i = j = k = 0
            while i < len(left) and j < len(right):
                if left[i] < right[j]:
                    arr[k] = left[i]
                    i += 1
                else:
                    arr[k] = right[j]
                    j += 1
                k += 1
            while i < len(left):
                arr[k] = left[i]
                i += 1
                k += 1
            while j < len(right):
                arr[k] = right[j]
                j += 1
                k += 1
            print(f"{arr}")
        return arr
    
    
# 时间复杂度 O(n) 级排序算法
# 计数排序、桶排序、基数排序
class Sort_Algorithm_O_n:
    """
    时间复杂度 O(n) 级排序算法
    包含计数排序、桶排序、基数排序
    """
    
    # 计数排序
    def counting_sort(arr):
        """
        使用计数排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        print("计数排序")
        max_val = max(arr) + 1  # 获取最大值
        count = [0] * max_val  # 初始化计数数组
        for num in arr:
            count[num] += 1  # 统计每个元素出现的次数
        sorted_arr = []
        for i, c in enumerate(count):
            sorted_arr.extend([i] * c)  # 根据计数填充排序后的数组
        print(f"{sorted_arr}")
        return sorted_arr
    
    # 桶排序
    def bucket_sort(arr):
        """
        使用桶排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        print("桶排序")
        bucket_count = len(arr)  # 桶的数量等于数组长度
        buckets = [[] for _ in range(bucket_count)]  # 初始化桶列表
        max_val = max(arr)
        for num in arr:
            index = int(num * bucket_count / (max_val + 1))  # 计算桶索引
            buckets[index].append(num)  # 将元素放入对应的桶中
            print(f"{buckets}")  # 打印当前桶状态
        sorted_arr = []
        for bucket in buckets:
            sorted_arr.extend(sorted(bucket))
        print(f"{sorted_arr}")
        return sorted_arr
    
    # 基数排序
    def radix_sort(arr):
        """
        使用基数排序算法对数组进行排序。
        
        参数:
            arr (list): 需要排序的数组。
        
        返回:
            list: 排序后的数组。
        """
        print("基数排序")
        max_val = max(arr)
        exp = 1
        while max_val // exp > 0:
           buckets = [[] for _ in range(10)]  # 初始化桶列表
           for num in arr:
               index = num // exp % 10
               buckets[index].append(num)
               print(f"{buckets}")  # 打印当前桶状态
           arr = [num for bucket in buckets for num in bucket]
           exp *= 10
           print(f"{arr}")
        return arr


# 示例
if __name__ == "__main__":
    """
    示例代码:
    随机生成一个数组，使用快速排序算法对其进行排序，并打印排序前后的结果。
    """
    # 随机生成数组
    array_length = random.randint(10, 11)  # 随机生成数组长度，范围为 xx 到 xx
    example = [random.randint(0, 100) for _ in range(array_length)]  # 随机生成数组内容，范围为 0 到 100

    print("原始数组:", example)
    
    start_time = time.time()  
    
    sorted_array = Sort_Algorithm_O_nlogn.quicksort(example) # 调用快速排序函数进行排序
    
    end_time = time.time() 
    
    print("排序后数组:", sorted_array)
    print(f"排序耗时: {end_time - start_time:.10f} 秒")  # 输出耗时（秒）