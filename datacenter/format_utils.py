def format_duration(seconds):
    duration = '%02d:%02d:%02d' % (seconds // 3600,
                                   (seconds % 3600) // 60,
                                   seconds  % 60)
    return duration
