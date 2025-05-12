expdp delassmvp/TU_PASSWORD schemas=DELASSMVP \
      directory=DATA_PUMP_DIR \
      dumpfile=DELASSMVP_backup_$(date +%Y%m%d%H%M).dmp \
      logfile=DELASSMVP_backup_$(date +%Y%m%d%H%M).log \
      compression=all
