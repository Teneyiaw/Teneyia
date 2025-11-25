import socket

def get_hostname_from_ip(ip_address):
    """
    Performs a reverse DNS lookup to get the hostname for a given IP address.
    """
    try:
        
        hostname_info = socket.gethostbyaddr(ip_address)
        
        
        hostname = hostname_info[0]
        
        
        result_list = [{
            "ip_address": ip_address, 
            "hostname": hostname
        }]
        
        return result_list
        
    except socket.herror as e:
        
        return [{
            "ip_address": ip_address, 
            "error": f"Error: No hostname found for this IP. ({e})"
        }]
    except Exception as e:
        
        return [{
            "ip_address": ip_address, 
            "error": f"An unexpected error occurred: {e}"
        }]


if __name__ == "__main__":
    

    user_ip = input("Enter an IP address (e.g., 8.8.8.8 or 192.168.1.1): ").strip()
    
    if not user_ip:
        print("IP address cannot be empty.")
    else:
        
        result = get_hostname_from_ip(user_ip)
        
        
        print("\n--- Resolution Result ---")
        if "error" in result[0]:
            print(f"IP: {result[0]['ip_address']}")
            print(f"Status: FAILED")
            print(f"Details: {result[0]['error']}")
        else:
            print(f"IP: {result[0]['ip_address']}")
            print(f"Hostname: **{result[0]['hostname']}**")
        
        
        print("\n--- Programmable List Output ---")
        print(result)
