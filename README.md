# Linux driver and daemon for Thermaltake Riing


## Compatibility
Python3 only.

Currently supported devices are (as they show up in thermaltakes TTRGBPLUS software:  
    Flow Riing RGB  
    Lumi Plus LED Strip  
    Pacific PR22-D5 Plus  
    Pacific Rad Plus LED Panel  
    Pacific V-GTX 1080Ti Plus GPU Waterblock  
    Pacific W4 Plus CPU Waterblock  
    Riing Plus  
If your's isn't listed, please create an issue and I'll implement it ASAP!!  


## Installation

### Pypi

`sudo pip3 install linux_thermaltake_rgb`  
The setup file will create the systemd unit
in `/usr/share/linux_thermaltake_rgb`  
you will need to copy these to the appropriate locations:

```bash
sudo cp /usr/share/linux_thermaltake_rgb/linux-thermaltake-rgb.service /usr/lib/systemd/system/

# and if this is a fresh install copy the default config file:
sudo mkdir /etc/linux_thermaltake_rgb/
sudo cp /usr/share/linux_thermaltake_rgb/config.yml /etc/linux_thermaltake_rgb/
```

### Arch linux

available in the aur as `linux-thermaltake-rgb`

### Starting and Enabling the Daemon

start and enable the systemd service  
`systemctl enable --now linux-thermaltake-rgb.service`  


## Configuration
the configuration file is expected to be in: `/etc/linux_thermaltake_rgb/config.yml`  
edit and configure suitably.  

example config is in `linux_thermaltake_rgb/assets/config.yml`

### Fan Manager Settings

- temp_target
  settings:
    sensor_name
    target
    multiplier
- locked_speed
  settings:
    speed
- curve
  settings:
    points
    
### Lighting Manager Settings

- alternating  
  settings:  
    speed  
    odd_rgb:  
      g  
      r  
      b  
    even_rgb:  
      g  
      r  
      b  
      
- temperature 
  settings: 
    speed 
    sensor_name 
    cold 
    hot 
    target 

- full 
  settings: 
    r 
    g 
    b 
    
- off 
  settings: 

- flow 
  settings: 
    speed 
    
- spectrum 
  settings: 
    speed 
    
- ripple 
  settings: 
    speed 
    r 
    g 
    b 
    
- blink 
  settings: 
    speed 
    r 
    g 
    b 
    
- pulse 
  settings: 
    speed 
    r 
    g 
    b 
  

