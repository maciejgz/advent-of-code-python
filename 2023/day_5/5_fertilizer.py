## https://adventofcode.com/2023/day/3
import re
import numpy as np


def read_file():
    with open("day_5/input.txt", "r") as file:
        # Read the entire file content into a single string
        return file.read()


def main():
    result = 0

    input = read_file()
    input_chars = []
    for line in input.split("\n"):
        if not line:
            input_chars.append('')
        else:
            input_chars.append(line)
            
    print(input_chars)
    
    ## input numebers 
    seeds = get_seeds(input_chars);
    
    ## seed-to-soil map:
    seeds_to_soil = get_mapping(input_chars, 'seed-to-soil map:')
    soil_to_ferrtilizer = get_mapping(input_chars, 'soil-to-fertilizer map:')
    fertilizer_to_water = get_mapping(input_chars, 'fertilizer-to-water map:')
    water_to_light = get_mapping(input_chars, 'water-to-light map:')
    light_to_temperature = get_mapping(input_chars, 'light-to-temperature map:')
    temp_to_humidity = get_mapping(input_chars, 'temperature-to-humidity map:')
    humidity_to_location = get_mapping(input_chars, 'humidity-to-location map:')
    
    results = []
    for seed in seeds:
        print("Seed: ", seed)
        soil = calulate_position(seed, seeds_to_soil)
        print("Soil: ", soil)
        fertilizer = calulate_position(soil, soil_to_ferrtilizer)
        print("Fertilizer: ", fertilizer)
        water = calulate_position(fertilizer, fertilizer_to_water)
        print("Water: ", water)
        light = calulate_position(water, water_to_light)
        print("Light: ", light)
        temperature = calulate_position(light, light_to_temperature)
        print("Temperature: ", temperature)
        humidity = calulate_position(temperature, temp_to_humidity)
        print("Humidity: ", humidity)
        location = calulate_position(humidity, humidity_to_location)
        print("Location: ", location)
        results.append(location)
        
    print(min(results))


def calulate_position(seed, mappings):
    print(seed, mappings)
    for mapping in mappings:
        if mapping[1] <= seed <= mapping[1] + mapping[2]:
            print("seed - mapping ", seed - mapping[1])
            return mapping[0] + seed - mapping[1]
        else:
            continue
    return seed
        

def get_seeds(input_line):
    input_numbers = input_line[0].replace('seeds: ', '').split()
    for i in range(len(input_numbers)):
        input_numbers[i] = int(input_numbers[i])
    return input_numbers


def get_mapping(lines, header):
    start_index = lines.index(header) + 1
    
    try:
        end_index = lines[start_index:].index('') + start_index
    except ValueError:  # No empty line found
        end_index = len(lines)
    
    map_lines = lines[start_index:end_index]
    
    map_data = []
    for line in map_lines:
        try:
            # Attempt to convert each element in the line to an integer
            map_data.append(list(map(int, line.split())))
        except ValueError:
            # Skip lines that cannot be converted to integers
            continue
    return map_data

if __name__ == "__main__":
    main()
