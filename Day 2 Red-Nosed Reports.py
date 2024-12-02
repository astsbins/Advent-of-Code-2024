#https://adventofcode.com/2024/day/2


def is_report_safe(report):
    if report[0] == report[1]:
        return (False,0)
    direction = -1
    if report[0] > report[1]:
        direction = 1
    
    for i in range(0,len(report)-1):
        if report[i]*direction <= report[i+1]*direction or report[i]*direction - report[i+1]*direction > 3:
            return (False,i)

    return (True,0)

def is_damped_reports_safe(report):
    report_copy =report.copy()
    safety = is_report_safe(report_copy)
    if safety[0] == True:
        return True
    else:
        print(f"popping {report_copy[safety[1]+1]} at {safety[1]+1} from report: {report_copy}")
        report_copy.pop(safety[1]+1)
        print(f"new report is {report_copy}, it is now {is_report_safe(report_copy)[0]}")
        if is_report_safe(report_copy)[0] == False:
            report_copy=report.copy()
            print(f"Retrying popping {report_copy[safety[1]]} at {safety[1]} from report: {report_copy}")
            report_copy.pop(safety[1])
            print(f"retried report is {report_copy}, it is now {is_report_safe(report_copy)[0]}")
            if is_report_safe(report_copy)[0] == False: ##if it is still false took backwards
                report_copy=report.copy()
                print(f"Retrying popping {report_copy[safety[1]]-1} at {safety[1]-1} from report: {report_copy}")
                report_copy.pop(safety[1]-1)
                print(f"retried report is {report_copy}, it is now {is_report_safe(report_copy)[0]}")
            print("")
            
        return is_report_safe(report_copy)[0]
            


with open('Day 2 inputs.txt') as f:
    safe_reports = 0
    dampend_safe_reports = 0
    for line in f:
        report = line.split(" ")
        report = [int(level) for level in report]
        safe_reports += is_report_safe(report)[0]
        dampend_safe_reports += is_damped_reports_safe(report)
    print(safe_reports)
    print(dampend_safe_reports)

    