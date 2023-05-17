function solution(id_list, report, k) {
  const reportTable = new Map();

  for (const userId of id_list) {
    reportTable.set(userId, new Set());
  }

  for (let i = 0; i < report.length; i++) {
    const data = report[i].trim().split(" ");
    const userId = data[0];
    const reportId = data[1];

    reportTable.get(userId).add(reportId);
  }

  const reportData = [...reportTable.entries()]
    .flatMap(([userId, reportList]) => [...reportList])
    .reduce((reportData, reportId) => {
      reportData[reportId] = ++reportData[reportId] || 1;
      return reportData;
    }, {});

  const finalReport = Object.keys(reportData).filter((data) => reportData[data] >= k);

  const emailResult = [];

  for (const userId of id_list) {
    let cnt = 0;
    for (const reportId of finalReport) {
      if (reportTable.get(userId).has(reportId)) {
        cnt++;
      }
    }
    emailResult.push(cnt);
  }

  return emailResult;
}

const id_list = ["muzi", "frodo", "apeach", "neo"];
const report = ["muzi frodo", "apeach frodo", "frodo neo", "muzi neo", "apeach muzi"];
k = 2;

solution(id_list, report, k);
