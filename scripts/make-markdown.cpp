#include <iostream>
#include <fstream>
#include <string>
#include <stack>
#include <sstream>
#include <utility> // std::pair
#include <map>

enum class ENV {
    OTHER = -1,         // Error handling
    DOCUMENT,           // Add to the write buffer as is until encountering a backslash
    CHAPTER,            // Put # before the chapter name
    SECTION,            // Put ## before the section name
    SUBSECTION,         // Put ### before the subsection name
    SUBSUBSECTION,      // Put #### before the subsubsection name
    INLINE_MATH,        // replace \( and \) with $$ and add the rest as is to the buffer
    MATH,               // replace \[ and \] with \n\n$$ and $$\n\n respectively and add the rest as is to the buffer
    BOLD,               // surround text with ** **
    ITALIC,             // surround text with _ _
    FIGURE              // ignore everything inside this environment
};

typedef std::map<ENV, std::pair<const std::string, const std::string>> MapType;

// Load the environment-ending map
void load_map(MapType& env_map);

// Figure out which environment to enter after encountering a backslash
void getEnvironment(std::stringstream& write, std::stack<ENV>& env, const std::string& line, int& i);

// Checks to see if the environment has ended, adds ending if it has
bool endEnvironment(MapType& env_map, std::stack<ENV>& env, 
                    std::stringstream& write, const std::string& line, int& i);

int main(int argc, char** argv) {
    // Extract the file name from the 1st command line argument
    std::string filename = std::string(argv[1]);

    // Input and output file paths (relative to scripts folder)
    std::string chapter = std::string("./chapters/").append(filename).append(".tex");
    std::string markdown = std::string("./markdown/").append(filename).append(".md");

    // Open input file
    std::ifstream fin(chapter, std::ios_base::in);

    // Open output file
    std::ofstream fout(markdown, std::ios_base::out);

    // Mapping of environment to <delimiter, ending> pair
    MapType env_map;
    load_map(env_map);

    // Environment stack, top tells current environment
    std::stack<ENV> env;
    // Start in the document environment
    env.push(ENV::DOCUMENT);
    
    
    if (fin.is_open()) {
        std::stringstream write;
        std::string line;
        // Loop through file line by line
        int line_no = 0;    // for debugging
        while (std::getline(fin, line) && line_no >= 0) {
            // Loop through the line character by character
            for (int i = 0; i < line.length(); i++) {
                // Check to see if the current environment has ended
                if (! endEnvironment(env_map, env, write, line, i) ) {
                        // check which environment to enter after encountering backslash
                        if (line[i] == '\\') {
                            getEnvironment(write, env, line, i);
                        }
                        // otherwise write to the buffer
                        else {
                            write << line[i];
                        }
                }
            }

            line_no++;
        }
        // write the buffer to the output file
        fout << write.str();
    }
    else {
        std::cout << "Failed to open " << chapter << std::endl;
    }

    return 0;
}

void load_map(MapType& env_map) {
    env_map.insert(MapType::value_type(ENV::DOCUMENT, std::make_pair("","")));
    env_map.insert(MapType::value_type(ENV::CHAPTER, std::make_pair("}","")));
    env_map.insert(MapType::value_type(ENV::SECTION, std::make_pair("}","")));
    env_map.insert(MapType::value_type(ENV::SUBSECTION, std::make_pair("}","")));
    env_map.insert(MapType::value_type(ENV::SUBSUBSECTION, std::make_pair("}","")));
    env_map.insert(MapType::value_type(ENV::INLINE_MATH, std::make_pair("\\)","$$")));
    env_map.insert(MapType::value_type(ENV::MATH, std::make_pair("\\]","$$\n")));
    env_map.insert(MapType::value_type(ENV::BOLD, std::make_pair("}","**")));
    env_map.insert(MapType::value_type(ENV::ITALIC, std::make_pair("}","_")));
}

struct Tag {
    const std::string tag;
    ENV environment;
    const std::string opening;
};

void getEnvironment(std::stringstream& write, std::stack<ENV>& env, 
                    const std::string& line, int& i) {
    // 'Environments' that don't start with begin, eg: \chapter{xyz}
    Tag tags[] = {
        {"chapter",ENV::CHAPTER, "# "},
        {"section",ENV::SECTION, "## "},
        {"subsection",ENV::SUBSECTION, "### "},
        {"subsubsection",ENV::SUBSUBSECTION, "#### "},
        {"textbf",ENV::BOLD, "**"},
        {"textemph",ENV::ITALIC, "_"}
    };
    for (auto &tag:tags) {
        // check the substring of line if it matches with the latex command
        if (line.compare(i+1,tag.tag.length(), tag.tag) == 0) {
            // move the pointer to the {
            i += tag.tag.length() + 1;
            env.push(tag.environment);
            write << tag.opening;
            return;
        }
    }
    // TODO: Environments that start with begin

    // Symbols after the backslash
    switch(line[i+1]) {
        case '(':
            i++;
            env.push(ENV::INLINE_MATH);
            write << "$$";
            break;
        case '[':
            i++;
            env.push(ENV::MATH);
            write << "\n\n$$";
            break;
        default:
            write << line[i];
            break;
    }
}

bool endEnvironment(MapType& env_map, std::stack<ENV>& env, 
                    std::stringstream& write, const std::string& line, int& i) {
    auto& delimiter = env_map[env.top()].first;
    auto& ending = env_map[env.top()].second;
    if (line[i] == delimiter[0]) {
        if (line.compare(i, delimiter.length(), delimiter) == 0) {
            i += delimiter.length() - 1;
            write << ending;
            env.pop();
            return true;
        }
    }
    return false;
}