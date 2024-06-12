import heapq
import csv

def parse_log_file(file_path):
    ip_counts = {}
    with open(file_path, 'r') as file:
        for line in file:
            line = line.strip()
            print(f"Processing line: '{line}'")  
            if not line:
                continue
            try:
                
                parts = line.split(',')
                if len(parts) != 3:
                    raise ValueError("Incorrect format")
                _, ip, count = parts
                ip = ip.strip()  
                count = int(count.strip()) 
                print(f"Parsed IP: '{ip}', Count: {count}")  
                if ip in ip_counts:
                    ip_counts[ip] += count
                else:
                    ip_counts[ip] = count
            except (ValueError, IndexError) as e:
                print(f"Skipping line due to error: {e}") 
                continue 
    print("Parsed IP Counts:", ip_counts)  
    return ip_counts

def get_top_n_ips(ip_counts, n):
    min_heap = []
    for ip, count in ip_counts.items():
        if len(min_heap) < n:
            heapq.heappush(min_heap, (count, ip))
        else:
            if count > min_heap[0][0] or (count == min_heap[0][0] and ip < min_heap[0][1]):
                heapq.heappushpop(min_heap, (count, ip))
    
    top_ips = sorted(min_heap, key=lambda x: (-x[0], x[1]))
    print("Top N IPs:", top_ips)
    return top_ips

def write_output(file_path, top_ips):
    with open(file_path, 'w', newline='') as file:
        writer = csv.writer(file)
        for rank, (count, ip) in enumerate(top_ips, start=1):
            writer.writerow([rank, ip, count])
    print(f"Output written to {file_path}")

def main(input_file, output_file, n):
    ip_counts = parse_log_file(input_file)
    top_ips = get_top_n_ips(ip_counts, n)
    write_output(output_file, top_ips)

if __name__ == "__main__":
    # Example usage
    input_file = 'c:/Users/Student/Desktop/Cysron/test_02.txt'
    output_file = 'c:/Users/Student/Desktop/Cysron/sample_result.txt'
    n = 3
    main(input_file, output_file, n)
