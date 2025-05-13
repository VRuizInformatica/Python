getMaxCutOffDate(): Observable<string> {
  return this.http
    .get<{ data: { DATA_CUT_OFF_DATE: string }[] }>(
      `${this.baseUrl}/securitized-assets?page=1&take=1`
    )
    .pipe(map(r => r.data[0]?.DATA_CUT_OFF_DATE ?? ''));
}
