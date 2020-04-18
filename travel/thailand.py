class ThailandPackage:
    def detail(self):
        print("[태국 패키지 3박 5일] 50만원")

if __name__ == "__main__":
    print("Thailand 모듈을 직접 실행하였음.")
    trip_to = ThailandPackage
    trip_to.detail
else:
    print("Thailand 모듈을 외부에서 실행하였음.")