

metrics = [
    "go_gc_duration_seconds",
    "go_goroutines",
    "go_info",
    "go_memstats_alloc_bytes",
    "go_memstats_alloc_bytes_total",
    "go_memstats_buck_hash_sys_bytes",
    "go_memstats_frees_total",
    "go_memstats_gc_cpu_fraction",
    "go_memstats_gc_sys_bytes",
    "go_memstats_heap_alloc_bytes",
    "go_memstats_heap_idle_bytes",
    "go_memstats_heap_inuse_bytes",
    "go_memstats_heap_objects",
    "go_memstats_heap_released_bytes",
    "go_memstats_heap_sys_bytes",
    "go_memstats_last_gc_time_seconds",
    "go_memstats_lookups_total",
    "go_memstats_mallocs_total",
    "go_memstats_mcache_inuse_bytes",
    "go_memstats_mcache_sys_bytes",
    "go_memstats_mspan_inuse_bytes",
    "go_memstats_mspan_sys_bytes",
    "go_memstats_next_gc_bytes",
    "go_memstats_other_sys_bytes",
    "go_memstats_stack_inuse_bytes",
    "go_memstats_stack_sys_bytes",
    "go_memstats_sys_bytes",
    "go_threads",
    "node_boot_time_seconds",
    "node_cpu_seconds_total",
    "node_disk_read_bytes_total",
    "node_disk_read_errors_total",
    "node_disk_read_retries_total",
    "node_disk_read_sectors_total",
    "node_disk_read_time_seconds_total",
    "node_disk_reads_completed_total",
    "node_disk_write_errors_total",
    "node_disk_write_retries_total",
    "node_disk_write_time_seconds_total",
    "node_disk_writes_completed_total",
    "node_disk_written_bytes_total",
    "node_disk_written_sectors_total",
    "node_exporter_build_info",
    "node_filesystem_avail_bytes",
    "node_filesystem_device_error",
    "node_filesystem_files",
    "node_filesystem_files_free",
    "node_filesystem_free_bytes",
    "node_filesystem_readonly",
    "node_filesystem_size_bytes",
    "node_load1",
    "node_load15",
    "node_load5",
    "node_memory_active_bytes",
    "node_memory_compressed_bytes",
    "node_memory_free_bytes",
    "node_memory_inactive_bytes",
    "node_memory_swap_total_bytes",
    "node_memory_swap_used_bytes",
    "node_memory_swapped_in_bytes_total",
    "node_memory_swapped_out_bytes_total",
    "node_memory_total_bytes",
    "node_memory_wired_bytes",
    "node_network_receive_bytes_total",
    "node_network_receive_errs_total",
    "node_network_receive_multicast_total",
    "node_network_receive_packets_total",
    "node_network_transmit_bytes_total",
    "node_network_transmit_errs_total",
    "node_network_transmit_multicast_total",
    "node_network_transmit_packets_total",
    "node_power_supply_battery_health",
    "node_power_supply_charging",
    "node_power_supply_current_ampere",
    "node_power_supply_current_capacity",
    "node_power_supply_info",
    "node_power_supply_max_capacity",
    "node_power_supply_power_source_state",
    "node_power_supply_present",
    "node_power_supply_time_to_empty_seconds",
    "node_power_supply_time_to_full_seconds",
    "node_scrape_collector_duration_seconds",
    "node_scrape_collector_success",
    "node_textfile_scrape_error",
    "node_thermal_cpu_available_cpu",
    "node_thermal_cpu_scheduler_limit_ratio",
    "node_thermal_cpu_speed_limit_ratio",
    "node_time_seconds",
    "node_time_zone_offset_seconds",
    "node_uname_info",
    "promhttp_metric_handler_errors_total",
    "promhttp_metric_handler_requests_in_flight",
    "promhttp_metric_handler_requests_total"
]

helpers = open("helpers/help.txt").read().splitlines()
types = open("helpers/types.txt").read().splitlines()


def enrich():
    complete_metrics = {}
    
    for metric in metrics:
        complete_metrics[metric] = {}
        for type in types:
            if metric in type:
                complete_metrics[metric]["type"] = type
                break
        for help in helpers:
            if metric in help:
                complete_metrics[metric]["help"] = help
                break
    
    
    return complete_metrics


if __name__ == "__main__":
    import json
    print(json.dumps(enrich(), indent=4))
