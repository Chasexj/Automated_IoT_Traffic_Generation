/*
 * Copyright nPrint 2020
 * Licensed under the Apache License, Version 2.0 (the "License"); you may not
 * use this file except in compliance with the License. You may obtain a copy
 * of the License at http://www.apache.org/licenses/LICENSE-2.0
 */

#ifndef FILE_WRITER
#define FILE_WRITER

#include <regex>
#include <errno.h>
#include <stdio.h>
#include <stdlib.h>
#include <string.h>
#include <sys/stat.h>
#include <sys/types.h>

#include "conf.hpp"
#include "ethernet_header.hpp"
#include "icmp_header.hpp"
#include "ipv4_header.hpp"
#include "ipv6_header.hpp"
#include "payload.hpp"
#include "tcp_header.hpp"
#include "udp_header.hpp"

/*
 * FileWriter takes care of output for all nPrints
 */

class FileWriter {
  public:
    void set_conf(Config c);
    void write_header(std::vector<std::string> header);
    void write_csv_stringvec(std::vector<std::string> &v);
    void write_bitstring_line(std::vector<std::string> &prefix,
                              std::vector<int8_t> &bistring_vec);
    void write_fields_line(std::vector<std::string> &prefix,
                           std::vector<std::string> &fields_vec);
    void write_line(std::string &line);

  private:
    void recursive_mkdir(char *path);
    FILE *fopen_mkdir(char *path);
    Config config;
    std::vector<uint32_t> keep_indexes;
    std::vector<std::string> build_bitstring_header(std::vector<std::string> header);
    uint32_t payload_len;
    FILE *outfile = NULL;
};

#endif
